use plotly::common::Mode;
use plotly::{color::NamedColor, Plot, Scatter};


pub fn plot_stock(x_values: Vec<f64>, y_values: Vec<f64>){
    println!("Grodyngel");

    // Create a scatter plot with two traces
    let trace = Scatter::new(x_values.clone(), y_values.clone())
        .mode(Mode::Lines)
        .name("Trace")
        .line(plotly::common::Line::new().color(NamedColor::Black).width(5 as f64).dash(plotly::common::DashType::LongDashDot));

    let mut plot = Plot::new();
    plot.add_trace(trace);
    plot.write_html("plot.html");
}