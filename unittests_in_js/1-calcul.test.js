/* eslint-disable */
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should return an int number', () => {
    assert.strictEqual(typeof calculateNumber(2.3, 3.1), 'number');
  });
  it('should return sum of num', () => {
    assert.strictEqual(calculateNumber('SUM', 2.2, 2, 3), 4);
  });
  it('should return sum', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });
  it('sum of nums', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('return sum of nums', () => {
    assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('sum', () => {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('sumNums', () => {
    assert.strictEqual(calculateNumber('SUM', -2, -2), -4);
  });
  it('sum negative', () => {
    assert.strictEqual(calculateNumber('SUM', -1.3, -4.5), -5);
  });
  it('sum decimals', () => {
    assert.strictEqual(calculateNumber('SUM', 0.4, 0.6), 1);
  });
  it('sum decimal', () => {
    assert.strictEqual(calculateNumber('SUM', 0.4, 0.2), 0);
  });
  it('sum main', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('should return subs of num', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 2.2, 2, 3), 0);
  });
  it('should return sub', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('sub of nums', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('return sub of nums', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('sub', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
  });
  it('subNums', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -2, -2), 0);
  });
  it('sub negative', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -1.3, -4.5), 3);
  });
  it('sub decimals', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 0.4, 0.6), -1);
  });
  it('sub decimal', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 0.4, 0.2), 0);
  });
  it('sub main', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });

  it('should return divs of num', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2.2, 2, 3), 1);
  });
  it('should return div', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
  });
  it('div of nums', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25);
  });
  it('return div of nums', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
  });
  it('div', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
  });
  it('divNums', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -2, -2), 1);
  });
  it('div negative', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -1.3, -4.5), 0.25);
  });
  it('div decimals', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0.4, 0.6), 0);
  });
  it('div decimal', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0.4, 0.2), 'Error');
  });
  it('div main1', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('div main2', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
