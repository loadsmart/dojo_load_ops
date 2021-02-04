package templategolang

import "testing"

func TestMain(t *testing.T) {
	tests := []struct {
		name     string
		number   Arabic
		expected Roman
	}{
		{
			name:     "1485 == MCDLXXXV",
			number:   1485,
			expected: "MCDLXXXV",
		},
		{
			name:     "998 == CM",
			number:   499,
			expected: "CDXCIX",
		},
		{
			name:     "499 == CDXCIX",
			number:   499,
			expected: "CDXCIX",
		},
		{
			name:     "99 == XCIX",
			number:   99,
			expected: "XCIX",
		},
		{
			name:     "49 == XLIX",
			number:   49,
			expected: "XLIX",
		},
		{
			name:     "9 == IX",
			number:   9,
			expected: "IX",
		},
		{
			name:     "358 == CCCLVIII",
			number:   358,
			expected: "CCCLVIII",
		},
		{
			name:     "4 == IV",
			number:   4,
			expected: "IV",
		},
		{
			name:     "51 == LI",
			number:   51,
			expected: "LI",
		},
		{
			name:     "1 == I",
			number:   1,
			expected: "I",
		},
		{
			name:     "2 == II",
			number:   2,
			expected: "II",
		},
		{
			name:     "3 == III",
			number:   3,
			expected: "III",
		},
		{
			name:     "5 == V",
			number:   5,
			expected: "V",
		},
		{
			name:     "10 == X",
			number:   10,
			expected: "X",
		},
		{
			name:     "20 == XX",
			number:   20,
			expected: "XX",
		},
		{
			name:     "30 == XXX",
			number:   30,
			expected: "XXX",
		},
		{
			name:     "500 == D",
			number:   500,
			expected: "D",
		},
		{
			name:     "100 == C",
			number:   100,
			expected: "C",
		},
		{
			name:     "200 == CC",
			number:   200,
			expected: "CC",
		},
		{
			name:     "300 == CCC",
			number:   300,
			expected: "CCC",
		},
		{
			name:     "1000 == M",
			number:   1000,
			expected: "M",
		},
		{
			name:     "2000 == MM",
			number:   2000,
			expected: "MM",
		},
		{
			name:     "3000 == MMM",
			number:   3000,
			expected: "MMM",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := romano(tt.number); got != tt.expected {
				t.Errorf("main() = %v, want %v", got, tt.expected)
			}
		})
	}
}
