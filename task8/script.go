package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	ticker := time.NewTicker(10 * time.Second)
	defer ticker.Stop()

	fmt.Printf("Hello, elapsed: %s\n", time.Since(start).Round(time.Second))

	for range ticker.C {
		fmt.Printf("Hello, elapsed: %s\n", time.Since(start).Round(time.Second))
	}
}