# Tayler_approximation

This Python script plots the Taylor polynomial of sin(x) for a given number of terms and compares it to the actual sin(x) function.

## Table of Contents

- [Introduction](#introduction)
- [Taylor Polynomials](#taylor-polynomials)
- [Usage](#usage)
- [Installation](#installation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, I've implemented a Python script to visualize the Taylor polynomial of sin(x). The Taylor polynomial is an approximation of a function using a polynomial with a finite number of terms.

## Taylor Polynomials

Taylor approximation, also known as Taylor series expansion, is a mathematical method used to approximate complex functions with simpler ones. It allows us to represent a function as an infinite sum of terms, where each term captures the behavior of the function around a specific point.

The basic idea is to find the derivatives of the function at a chosen point (usually denoted as "a"). These derivatives provide information about the function's rate of change at that point. The Taylor approximation then constructs a polynomial around "a" using these derivatives. The more terms we include in the polynomial, the better the approximation becomes.

The Taylor approximation of a function "f(x)" at point "a" is given by:

f(x) ≈ f(a) + f'(a)(x - a) + (f''(a)/2!)(x - a)^2 + (f'''(a)/3!)(x - a)^3 + ...

Here:
- f(a) is the value of the function at point "a."
- f'(a), f''(a), f'''(a), etc., are the derivatives of the function at point "a."
- (x - a)^n represents the distance from the point "a."

The Taylor approximation is useful for simplifying complex functions and approximating their behavior around a particular point. As we include more terms in the polynomial, the approximation becomes more accurate. However, it's important to note that the Taylor series may not converge for some functions or may converge only in a limited range around the chosen point.]

## Example 

For simplicity, let's use the sine-wave function to demonstrate how Taylor's approximation works. By increasing the number of gradients we consider, we can achieve a more accurate approximation of the function. In the plots below, I've shown the approximations for T=1, T=3, T=5, T=15, and T=50.

![taylor_approx](https://github.com/IoannisTselekoglou/Tayler_approximation-/assets/56356882/93e02cd9-8d85-4eee-b77e-7e0caf8a6b5f)

As you can observe, the approximated function progressively improves its accuracy in matching the sine function, especially within a small value range. Even for T=5, the approximation already achieves a fairly accurate representation.

## Installation

1. Clone this repository.
2. Install the required dependencies using pip:
    pip install matplotlib
    pip install numpy 

