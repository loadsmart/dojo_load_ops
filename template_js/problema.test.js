// Mantenha o seu cursor aqui: |

const mapping = [
    [1000, 'M'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I'],
]

function romano(number) {
    let ret = ''

    mapping.forEach(([arabic, roman]) => {
        while (number >= arabic) {
            ret += roman
            number -= arabic
        }
    })

    return ret
}

test('1485 == MCDLXXXV', () => {
    expect(romano(1485)).toBe('MCDLXXXV');
});

test('998 == CM', () => {
    expect(romano(499)).toBe('CDXCIX');
});

test('499 == CDXCIX', () => {
    expect(romano(499)).toBe('CDXCIX');
});

test('99 == XCIX', () => {
    expect(romano(99)).toBe('XCIX');
});

test('49 == XLIX', () => {
    expect(romano(49)).toBe('XLIX');
});

test('9 == IX', () => {
    expect(romano(9)).toBe('IX');
});

test('358 == CCCLVIII', () => {
    expect(romano(358)).toBe('CCCLVIII');
});

test('4 == IV', () => {
    expect(romano(4)).toBe('IV');
});

test('51 == LI', () => {
    expect(romano(51)).toBe('LI');
});

test('1 == I', () => {
    expect(romano(1)).toBe('I');
});

test('2 == II', () => {
    expect(romano(2)).toBe('II');
});

test('3 == III', () => {
    expect(romano(3)).toBe('III');
});

test('5 == V', () => {
    expect(romano(5)).toBe('V');
});

test('10 == X', () => {
    expect(romano(10)).toBe('X');
});

test('20 == XX', () => {
    expect(romano(20)).toBe('XX');
});

test('30 == XXX', () => {
    expect(romano(30)).toBe('XXX');
});

test('500 == D', () => {
    expect(romano(500)).toBe('D');
});

test('100 == C', () => {
    expect(romano(100)).toBe('C');
});

test('200 == CC', () => {
    expect(romano(200)).toBe('CC');
});

test('300 == CCC', () => {
    expect(romano(300)).toBe('CCC');
});

test('1000 == M', () => {
    expect(romano(1000)).toBe('M');
});

test('2000 == MM', () => {
    expect(romano(2000)).toBe('MM');
});

test('3000 == MMM', () => {
    expect(romano(3000)).toBe('MMM');
});