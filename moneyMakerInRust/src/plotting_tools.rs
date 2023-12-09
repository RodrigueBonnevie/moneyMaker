use plotly::common::Mode;
use plotly::{color::NamedColor, Plot, Scatter};

use crate::parse_json::StockData;

pub fn stock_data_to_vector(stock_data: &StockData) -> (Vec<f64>, Vec<f64>) {
    let mut y_values: Vec<f64> = vec![];
    let mut x_values: Vec<f64> = vec![];

    let mut iterations: f64 = 0.0;
    for day in stock_data.time_series.iter() {
        let stock_price: f64 = day.1.close.parse().unwrap();
        x_values.push(iterations);
        y_values.push(stock_price);
        iterations += 1.0;
    }

    (x_values, y_values)
}

pub fn plot_stock(file_name: &str, x_values: Vec<f64>, y_values: Vec<f64>) {
    let trace = Scatter::new(x_values.clone(), y_values.clone())
        .mode(Mode::Lines)
        .name("Trace")
        .line(
            plotly::common::Line::new()
                .color(NamedColor::Black)
                .width(2 as f64),
        );

    let mut plot = Plot::new();
    plot.add_trace(trace);
    plot.write_html(format!("{}.html", file_name));
}

pub fn plot_buy_signal(
    file_name: &str,
    stock_price: (Vec<f64>, Vec<f64>),
    buy_days: (Vec<f64>, Vec<f64>),
) {
    let trace_price = Scatter::new(stock_price.0.clone(), stock_price.1.clone())
        .mode(Mode::Lines)
        .name("Stock price")
        .line(
            plotly::common::Line::new()
                .color(NamedColor::Black)
                .width(1 as f64),
        );
    let trace_buy = Scatter::new(buy_days.0.clone(), buy_days.1.clone())
        .mode(Mode::Markers)
        .name("Buying days");

    let mut plot = Plot::new();
    plot.add_trace(trace_price);
    plot.add_trace(trace_buy);
    plot.write_html(format!("{}.html", file_name));
}
