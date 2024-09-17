package main

import (
	"fmt"
)

// TreeNode represents a node in a binary tree.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// sumNumbers function calculates the sum of all numbers formed by root-to-leaf paths.
func sumNumbers(root *TreeNode) int {
	var dfs func(node *TreeNode, currentNumber int) int

	dfs = func(node *TreeNode, currentNumber int) int {
		if node == nil {
			return 0
		}

		currentNumber = currentNumber*10 + node.Val

		if node.Left == nil && node.Right == nil {
			return currentNumber
		}

		return dfs(node.Left, currentNumber) + dfs(node.Right, currentNumber)
	}

	return dfs(root, 0)
}

func main() {
	// Example usage:
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}

	result := sumNumbers(root)
	fmt.Printf("result: %d\n", result)
}
