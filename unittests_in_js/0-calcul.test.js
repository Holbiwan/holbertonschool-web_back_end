/* eslint-disable */
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return an int number', () => {
    assert.strictEqual(typeof calculateNumber(2.3, 3.1), 'number');
  });
  it('should return sum of num', () => {
    assert.strictEqual(calculateNumber(2.2, 2, 3), 4);
  });
  it('should return sum', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('sum of nums', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it('return sum of nums', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('sum', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('sumNums', () => {
    assert.strictEqual(calculateNumber(-2, -2), -4);
  });
  it('sum negative', () => {
    assert.strictEqual(calculateNumber(-1.3, -4.5), -5);
  });
  it('sum decimals', () => {
    assert.strictEqual(calculateNumber(0.4, 0.6), 1);
  });
  it('sum decimal', () => {
    assert.strictEqual(calculateNumber(0.4, 0.2), 0);
  });
});
