use crate::moving_average::MovingAverage;
use crate::parse_json::StockData;
use crate::plotting_tools::{plot_stock, stock_data_to_vector};

pub fn momentum_trading(long_avg: u32, short_avg: u32, stock_data: &StockData) {
    println!(
        "{} , {} , {}",
        long_avg, short_avg, stock_data.meta_data.symbol
    );
    let mut moving_average = MovingAverage::new(5.0);
    for day in stock_data.time_series.iter() {
        moving_average.update(day.1.close.parse().unwrap());
    }
    let (x_values, y_values) = stock_data_to_vector(stock_data);
    plot_stock(&stock_data.meta_data.symbol, x_values, y_values);
}
