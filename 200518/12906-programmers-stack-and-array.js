// https://programmers.co.kr/learn/courses/30/lessons/12906
// 배열의 중복 처리 문제
// Stack 클래스를 만들어 해결.

class Stack {
  constructor() {
      this.arr = [];
  }
  
  isEmpty() {
      return this.arr.length === 0
  }
  
  push(el) {
      this.arr.push(el);
  }
  
  top() {
      if (this.isEmpty()) {
          return false;
      } else {
          return this.arr[this.arr.length - 1]
      }
  }
  
  getArr() {
      return this.arr;
  }
}

function handleElement(el, stack) {
  if (stack.isEmpty()) {
      // push element
      stack.push(el);
  } else if (stack.top() === el) {
      // continue
  } else {
      // push element
      stack.push(el);
  }
}

function solution(arr)
{
  const stack = new Stack();
  
  arr.map(el => handleElement(el, stack));
  
  return stack.getArr();
}