use std::collections::LinkedList;

pub fn add_two_numbers(l1: &LinkedList<i64>, l2: &LinkedList<i64>) -> LinkedList<i64> {
    let together = l1.iter().zip(l2.iter());

    let mut sum: LinkedList<i64> = LinkedList::new();

    let mut ten = false;
    for tuple in together {
        let s = tuple.0 + tuple.1 + if ten { 1 } else { 0 };
        sum.push_back(if s >= 10 {
            ten = true;
            s - 10
        } else {
            ten = false;
            s
        })
    }
    if ten {
        sum.push_back(1)
    }

    sum
}
