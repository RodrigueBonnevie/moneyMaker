extern crate serde;
extern crate serde_json;

use crate::wallet::Wallet;

mod algorithms;
mod moving_average;
mod parse_json;
mod plotting_tools;
mod wallet;

fn main() {
    println!("Grodan och paddan");
    //let file_name: &str = "../data/lilSPY.json";
    let file_name: &str = "C:/Users/Rodri/Projects/moneyMaker/data/SPY.json";
    let stock_data =
        parse_json::get_stock_data_from_json(file_name).expect("Couldn't get data from json file");
    algorithms::momentum_trading(10, 5, &stock_data);
    let mut wallet: Wallet = Wallet::new(1000.0);
    wallet.buy_stock(50.0, 1.0, "Groda");
    println!("Money in wallet {} ", wallet.get_liquid_assets());
    wallet.sell_stock(6.0, "Groda");
    println!("Money in wallet {} ", wallet.get_liquid_assets());
    wallet.sell_stock(6.0, "Groda");
    println!("Money in wallet {} ", wallet.get_liquid_assets());
}
