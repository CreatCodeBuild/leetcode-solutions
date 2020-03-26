mod p2;
// use std::boxed::Box;
use std::collections::LinkedList;

fn main() {
    let mut list1: LinkedList<i64> = LinkedList::new();
    list1.push_back(4);
    list1.push_back(2);
    let mut list2: LinkedList<i64> = LinkedList::new();
    list2.push_back(6);
    list2.push_back(7);
    for n in p2::add_two_numbers(&list1, &list2).iter() {
        println!("{}", n)
    }
}
