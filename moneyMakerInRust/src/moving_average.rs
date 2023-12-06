#[derive(Clone, Copy)]
pub struct MovingAverage {
    sample_length: f64,
    pub current_average: f64,
    points_calculated: u32,
}

impl MovingAverage {
    pub fn new(sample_length: f64) -> MovingAverage {
        MovingAverage {
            sample_length: (sample_length),
            current_average: (0.0),
            points_calculated: 0,
        }
    }

    pub fn update(&mut self, new_sample: f64, popped_sample: f64) {
        self.current_average += new_sample / self.sample_length;
        self.current_average -= popped_sample / self.sample_length;
        self.points_calculated += 1;
    }

    pub fn get_moving_average(self) -> f64 {
        self.current_average.clone()
    }
}
