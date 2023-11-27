use crate::parse_json::StockData;

pub fn moving_average(long_avg: u32, short_avg: u32, stock_data: &StockData) {
    println!(
        "{} , {} , {}",
        long_avg, short_avg, stock_data.meta_data.symbol
    );
}
