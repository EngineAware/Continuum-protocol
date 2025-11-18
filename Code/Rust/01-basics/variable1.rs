fn main() { 
     let mut x=5; // 'mut' makes it mutable
     let y=20;// immutable
     x=y+x; // we change x
     let name:&str="System";

     println!("y={}",y);
     println!("x={}",x);
     println!("Hello {}",name);
}
