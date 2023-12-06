extern crate queues;
use queues::*;

pub struct MovingAverage {
    sample_length: f64,
    pub current_average: f64,
    processed_values: Queue<f64>,
}

impl MovingAverage {
    pub fn new(sample_length: f64) -> MovingAverage {
        MovingAverage {
            sample_length: (sample_length),
            current_average: (0.0),
            processed_values: queue![],
        }
    }

    pub fn update(&mut self, new_sample: f64) {
        self.processed_values.add(new_sample).expect("couldn't add value");
        self.current_average += new_sample / self.sample_length;
        if self.processed_values.size() > self.sample_length as usize{
           let outgoing_value = self.processed_values.remove().expect("queue empty");
            self.current_average -= outgoing_value / self.sample_length;
        }
    }

    pub fn get_moving_average(&self) -> f64 {
        self.current_average 
    }
}
