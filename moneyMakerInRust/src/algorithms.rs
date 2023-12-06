use crate::moving_average::MovingAverage;
use crate::parse_json::StockData;

pub fn groda(long_avg: u32, short_avg: u32, stock_data: &StockData) {
    println!(
        "{} , {} , {}",
        long_avg, short_avg, stock_data.meta_data.symbol
    );
    let mut moving_average = MovingAverage::new(5.0);
    moving_average.update(5.0, 0.0);
    println!("Average: {}", moving_average.get_moving_average());
}
