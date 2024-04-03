function solution(array, commands) {
    var answer = [];
    
    for (let com of commands) {
        let [i, j, k] = com
        let newArray = array.slice(i-1, j)
        newArray.sort((a, b) => a - b)
        answer.push(newArray[k-1])
    }
    
    return answer;
}