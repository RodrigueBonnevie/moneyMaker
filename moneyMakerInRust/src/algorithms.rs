use crate::moving_average::MovingAverage;
use crate::parse_json::StockData;
use crate::plotting_tools::{plot_buy_signal, plot_stock, stock_data_to_vector};

pub fn momentum_trading(long_avg: u32, short_avg: u32, stock_data: &StockData) {
    println!(
        "{} , {} , {}",
        long_avg, short_avg, stock_data.meta_data.symbol
    );
    let mut moving_average_200 = MovingAverage::new(200.0);
    let mut moving_average_50 = MovingAverage::new(50.0);
    let mut buy_days: Vec<f64> = vec![];
    let mut buy_price: Vec<f64> = vec![];
    let mut day_number: f64 = 0.0;
    for day in stock_data.time_series.iter() {
        moving_average_200.update(day.1.close.parse().unwrap());
        moving_average_50.update(day.1.close.parse().unwrap());
        if moving_average_200.get_moving_average() < moving_average_50.get_moving_average() {
            buy_days.push(day_number);
            buy_price.push(day.1.close.parse().unwrap());
        }
        day_number += 1.0;
    }

    let (x_values, y_values) = stock_data_to_vector(stock_data);
    // plot_stock(&stock_data.meta_data.symbol, x_values, y_values);
    plot_buy_signal("Buy", (x_values, y_values), (buy_days, buy_price));
}
