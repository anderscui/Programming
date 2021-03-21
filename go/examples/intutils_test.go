package main

import (
	"fmt"
	"testing"
)

func MinInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func TestMinIntBasic(t *testing.T)  {
	ans := MinInt(2, -2)
	if ans != -2 {
		t.Errorf("MinInt(2, -2) = %d; want -2", ans)
	}
}

func TestMinIntTableDriven(t *testing.T) {
	var tests = []struct{
		a, b int
		want int
	} {
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{-1, 0, 0},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := MinInt(tt.a, tt.b)
			if ans != tt.want {
				t.Errorf("MinInt(%d, %d) = %d; want %d", tt.a, tt.b, ans, tt.want)
			}
		})
	}
}