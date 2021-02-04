// Package templategolang is a template to Golang coding dojo
package templategolang

type Arabic int //int64?
type Roman string
type Par struct {
	arabic Arabic
	roman  Roman
}

var mapping = []Par{
	{arabic: 1000, roman: "M"},
	{arabic: 500, roman: "D"},
	{arabic: 400, roman: "CD"},
	{arabic: 100, roman: "C"},
	{arabic: 90, roman: "XC"},
	{arabic: 50, roman: "L"},
	{arabic: 40, roman: "XL"},
	{arabic: 10, roman: "X"},
	{arabic: 9, roman: "IX"},
	{arabic: 5, roman: "V"},
	{arabic: 4, roman: "IV"},
	{arabic: 1, roman: "I"},
}

func romano(number Arabic) Roman {
	ret := Roman("")

	for _, par := range mapping {
		arabic := par.arabic
		roman := par.roman

		for number >= arabic {
			ret += roman
			number -= arabic
		}
	}

	return ret
}
