// Package templategolang is a template to Golang coding dojo
package templategolang

import "strconv"

func oneCounter(number uint) uint {
	concatNumbers := ""
	for i := 1; i <= int(number); {
		concatNumbers += strconv.Itoa(i)
		i++
	}
	// for ;; {

	// }
	count := uint(0)
	// nil
	// var count uint
	for _, v := range concatNumbers {

		if v == '1' {
			count++
		}
	}
	return count
}

// Interfaces

type Example interface {
	oneCounter(number uint) uint
}

type MileageGetter interface {
	oneCounter(number uint) uint
}

// struct

type contador struct { //implements Example
	name string
}

func (c contador) oneCounter(number uint) uint {
	return number
}

func (c contador) oneCounter2(number int) int {
	return number
}

//  teste := contador{name: "aaaaa"}
//  temp := MileageGetter(teste)
// teste.oneCounter(...)
