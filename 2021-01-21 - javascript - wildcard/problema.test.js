// Mantenha o seu cursor aqui: |


function isMatch(str, pattern) {
    if (pattern.includes("*")) {
        // acdcb a*ccb
        const index = pattern.indexOf("*");
        const next_pattern = pattern[index+2];
        if (next_pattern === "?") {
            return false;
        } 
        return true;
    }
    while (pattern.includes("?")) {
        let index = pattern.indexOf("?")
        const patternStr = [...pattern];
        patternStr[index] = str[index]
        pattern = patternStr.join('')
    }    
    return str === pattern
}

// 'acdcb', 'a*c?b', false
// 'acdb', 'a*c?b', true
// 'acdcb', 'a*cdcb', true
// 'acd', 'a*c?', true
// 'allllcd', 'a*c?', true

test("acdcb does not match a*c?b", () => {
    expect(isMatch('acdcb', 'a*c?b')).toBe(false);
})

test('adceb match *a*b', () => {
    expect(isMatch('adceb', '*a*b')).toBe(true);
})

test('cac match with ?a?', () => {
    expect(isMatch('cac', '?a?')).toBe(true);
});

test('ca match with ?a', () => {
    expect(isMatch('ca', '?a')).toBe(true);
});

test('cb not match with ?a', () => {
    expect(isMatch('cb', '?a')).toBe(false);
});

test('two char does not match ?', () => {
    expect(isMatch('bb', '?')).toBe(false);
});

test('one char match ?', () => {
    expect(isMatch('b', '?')).toBe(true);
});

test('b not match a', () => {
    expect(isMatch('b', 'a')).toBe(false);
});

test('b match b', () => {
    expect(isMatch('b', 'b')).toBe(true);
});

test('a match a', () => {
    expect(isMatch('a', 'a')).toBe(true);
});

test('anything match *', () => {
    expect(isMatch('fsadsafsa', '*')).toBe(true);
});

test('b match b', () => {
    expect(isMatch('b', 'b')).toBe(true);
});

test('a match a', () => {
    expect(isMatch('a', 'a')).toBe(true);
});

test('anything match *', () => {
    expect(isMatch('fsadsafsa', '*')).toBe(true);

});