extern crate serde;
extern crate serde_json;

use std::collections::BTreeMap;

use serde::Deserialize;
use serde_json::Result;

#[derive(Deserialize)]
struct StockMetaData {
    #[serde(rename = "1. Information")]
    information: String,
    #[serde(rename = "2. Symbol")]
    symbol: String,
    #[serde(rename = "3. Last Refreshed")]
    last_refreshed: String,
    #[serde(rename = "4. Output Size")]
    output_size: String,
    #[serde(rename = "5. Time Zone")]
    time_zone: String,
}

#[derive(Deserialize)]
struct TimeSeries {
    #[serde(rename = "1. open")]
    open: String,
    #[serde(rename = "2. high")]
    high: String,
    #[serde(rename = "3. low")]
    low: String,
    #[serde(rename = "4. close")]
    close: String,
    #[serde(rename = "5. volume")]
    volume: String,
}

#[derive(Deserialize)]
struct StockData {
    #[serde(rename = "Meta Data")]
    meta_data: StockMetaData,
    #[serde(rename = "Time Series (Daily)")]
    time_series: BTreeMap<String, TimeSeries>,
}

fn get_stock_data_from_json(file_name: &str) -> Result<StockData> {
    let file_contents: String =
        std::fs::read_to_string(file_name).expect("Couldn't read json file");

    let stock_data: StockData = serde_json::from_str(&file_contents)?;

    Ok(stock_data)
}

fn print_stock_data(stock_data: StockData) {
    for day in stock_data.time_series.iter() {
        println!(
            "On {} {} closed at {}",
            day.0, stock_data.meta_data.symbol, day.1.close
        );
    }
}

fn main() {
    println!("Grodan och paddan");
    let file_name: &str = "C:/Users/Rodri/Projects/moneyMaker/data/SPY.json";
    let stock_data = get_stock_data_from_json(file_name).expect("Couldn't get data from json file");
    print_stock_data(stock_data);
}
