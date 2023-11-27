use std::collections::BTreeMap;

use serde::Deserialize;
use serde_json::Result;

#[derive(Deserialize)]
pub struct StockMetaData {
    #[serde(rename = "1. Information")]
    pub information: String,
    #[serde(rename = "2. Symbol")]
    pub symbol: String,
    #[serde(rename = "3. Last Refreshed")]
    pub last_refreshed: String,
    #[serde(rename = "4. Output Size")]
    pub output_size: String,
    #[serde(rename = "5. Time Zone")]
    pub time_zone: String,
}

#[derive(Deserialize)]
pub struct TimeSeries {
    #[serde(rename = "1. open")]
    pub open: String,
    #[serde(rename = "2. high")]
    pub high: String,
    #[serde(rename = "3. low")]
    pub low: String,
    #[serde(rename = "4. close")]
    pub close: String,
    #[serde(rename = "5. volume")]
    pub volume: String,
}

#[derive(Deserialize)]
pub struct StockData {
    #[serde(rename = "Meta Data")]
    pub meta_data: StockMetaData,
    #[serde(rename = "Time Series (Daily)")]
    pub time_series: BTreeMap<String, TimeSeries>,
}

pub fn get_stock_data_from_json(file_name: &str) -> Result<StockData> {
    let file_contents: String =
        std::fs::read_to_string(file_name).expect("Couldn't read json file");

    let stock_data: StockData = serde_json::from_str(&file_contents)?;

    Ok(stock_data)
}

pub fn print_stock_data(stock_data: &StockData) {
    for day in stock_data.time_series.iter() {
        println!(
            "On {} {} closed at {}",
            day.0, stock_data.meta_data.symbol, day.1.close
        );
    }
}
