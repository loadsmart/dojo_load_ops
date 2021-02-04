//Parking: |
package templategolang

import "testing"

func TestMain(t *testing.T) {
	tests := []struct {
		name     string
		number   uint
		expected uint
	}{
		{
			name:     "Case 0",
			number:   0,
			expected: 0,
		},
		{
			name:     "Case 1",
			number:   1,
			expected: 1,
		},
		{
			name:     "Case 2",
			number:   2,
			expected: 1,
		},
		{
			name:     "Case 3",
			number:   7,
			expected: 1,
		},
		{
			name:     "Case 4",
			number:   10,
			expected: 2,
		},
		{
			name:     "Case 5",
			number:   11,
			expected: 4,
		},
		{
			name:     "Case 6",
			number:   12,
			expected: 5,
		},
		{
			name:     "Case 8",
			number:   19,
			expected: 12,
		},
		{
			name:     "Case 9",
			number:   29,
			expected: 13,
		},
		{
			name:     "Case 10",
			number:   39,
			expected: 14,
		},
		{
			name:     "Case 11",
			number:   99,
			expected: 20,
		},
		{
			name:     "Case 12",
			number:   100,
			expected: 21,
		},
		{
			name:     "Case 13",
			number:   101,
			expected: 23,
		},
		{
			name:     "Case 13",
			number:   109,
			expected: 31,
		},
		{
			name:     "Case 14",
			number:   111,
			expected: 36,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := oneCounter(tt.number); got != tt.expected {
				t.Errorf("%s , result = %v, want %v", tt.name, got, tt.expected)
			}
		})
	}
}
