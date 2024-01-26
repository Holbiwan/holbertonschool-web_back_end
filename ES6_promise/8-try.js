// Throw an error if denominator is equal to 0 
export default function divideFunction(numerator, denominator) {
    if (denominator === 0) {
      throw new Error('cannot divide by 0');
    }
    return numerator / denominator;
  }  
