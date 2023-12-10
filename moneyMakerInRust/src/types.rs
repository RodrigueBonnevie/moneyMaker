use serde::Deserialize;
use std::collections::BTreeMap;

#[derive(Deserialize)]
pub struct StockData {
    #[serde(rename = "Meta Data")]
    pub meta_data: StockMetaData,
    #[serde(rename = "Time Series (Daily)")]
    pub time_series: BTreeMap<String, TimeSeries>,
}

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
