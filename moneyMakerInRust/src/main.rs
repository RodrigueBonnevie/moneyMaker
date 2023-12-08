extern crate serde;
extern crate serde_json;

mod algorithms;
mod moving_average;
mod parse_json;
mod plotting_tools;

fn main() {
    println!("Grodan och paddan");
    //let file_name: &str = "../data/lilSPY.json";
    let file_name: &str = "C:/Users/Rodri/Projects/moneyMaker/data/SPY.json";
    let stock_data =
        parse_json::get_stock_data_from_json(file_name).expect("Couldn't get data from json file");
    algorithms::momentum_trading(10, 5, &stock_data)
}
