function tailRecursiveSum(numberArray,result){
    if(numberArray.length === 1){
        return result;
    }else{
        numberArray.shift();
        return tailRecursiveSum(numberArray,result+numberArray[0])
    }
}

var array = [1,2,3,4];
let result = tailRecursiveSum(array,0);
console.log(result);