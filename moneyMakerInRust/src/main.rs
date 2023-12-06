extern crate serde;
extern crate serde_json;

mod algorithms;
mod moving_average;
mod parse_json;
mod plotting_tools;

fn main() {
    println!("Grodan och paddan");
    let file_name: &str = "../data/lilSPY.json";
    let stock_data =
        parse_json::get_stock_data_from_json(file_name).expect("Couldn't get data from json file");
    parse_json::print_stock_data(&stock_data);
    let x_values: Vec<f64> = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let y_values: Vec<f64> = vec![2.0, 4.0, 3.0, 1.0, 5.0];
    plotting_tools::plot_stock(x_values, y_values);
    algorithms::groda(10, 5, &stock_data)
}
