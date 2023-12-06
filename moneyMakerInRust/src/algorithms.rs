use crate::moving_average::MovingAverage;
use crate::parse_json::StockData;

pub fn groda(long_avg: u32, short_avg: u32, stock_data: &StockData) {
    println!(
        "{} , {} , {}",
        long_avg, short_avg, stock_data.meta_data.symbol
    );
    let mut moving_average = MovingAverage::new(5.0);
    for day in stock_data.time_series.iter() {
        moving_average.update(day.1.close.parse().unwrap());
        println!(
            "On {} {} closed at {} moving average is {}",
            day.0, stock_data.meta_data.symbol, day.1.close, moving_average.get_moving_average()
        );
    }
}
