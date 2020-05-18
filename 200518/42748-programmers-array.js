// https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript#
// 배열을 조작하는 문제
// array Array.slice(), Array.sort() 사용

function sortArray(el, array) {
  let i, j, k;
  [i,j,k] = el;
  
  array = array
      .slice(i-1,j)
      .sort((a,b) => a-b);
  
  return array[k-1];
}

function solution(array, commands) {
  var answer = [];
  
  answer = commands.map(el => sortArray(el, array))
  
  return answer;
}