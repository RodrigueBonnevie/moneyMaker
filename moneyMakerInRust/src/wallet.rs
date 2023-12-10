use std::collections::HashMap;
pub struct Wallet {
    liquid_assets: f64,
    stock_assets: HashMap<String, f64>,
}

impl Wallet {
    pub fn new(money: f64) -> Wallet {
        Wallet {
            liquid_assets: (money),
            stock_assets: HashMap::new(),
        }
    }
    pub fn buy_stock(&mut self, price: f64, amount: f64, symbol: &str) {
        self.liquid_assets -= price * amount;
        self.stock_assets.insert(symbol.to_string(), amount);
    }

    pub fn sell_stock(&mut self, price: f64, symbol: &str) {
        if self.stock_assets.contains_key(symbol) {
            let amount_of_stock = self.stock_assets.remove(symbol).expect("Stock not owned");
            self.liquid_assets += price * amount_of_stock;
        }
    }
    pub fn is_stock_owned(&self, symbol: &str) -> bool {
        self.stock_assets.contains_key(symbol)
    }

    pub fn get_liquid_assets(&self) -> f64 {
        self.liquid_assets
    }
}
