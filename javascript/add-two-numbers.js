/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    let carry = 0
    let result = null;
    let trav = null;
    let val1, val2;

    while (l1 !== null || l2 !== null) {
        val1 = 0;
        if (l1 !== null) {
            val1 = l1.val;
            l1 = l1.next;
        } // if

        val2 = 0;
        if (l2 !== null) {
            val2 = l2.val;
            l2 = l2.next;
        } // if

        let sum = val1 + val2 + carry;
        carry = Math.trunc(sum / 10);
        sum = sum % 10;

        let node = new ListNode(sum);
        if (result === null) {
            result = trav = node;
        } else {
            trav.next = node;
            trav = node;
        } // else
    } // while

    if (carry !== 0) {
        trav.next = new ListNode(carry);
    } // if

    return result;
};

// test here
var l1 = createListNode([9,9,9,9,9,9,9]);
var l2 = createListNode([9,9,9, 9]);
var result = addTwoNumbers(l1, l2);

while (result !== null) {
    console.log(result.val);
    result = result.next;
} // while

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
} // ListNode

function createListNode(nums) {
    let head = null;
    let trav = null;

    for (let i = 0; i < nums.length; i++) {
        let node = new ListNode(nums[i]);

        if (head) {
            trav.next = node;
            trav = node;
        } else {
            head = trav = node;
        } // else
    } // for

    return head;
} // createListNode
