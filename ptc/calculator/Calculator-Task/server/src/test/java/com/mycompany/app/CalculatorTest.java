package com.mycompany.app;

import static org.hamcrest.CoreMatchers.is;
import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat;


public class CalculatorTest {

    double answer;

    @Test
    public void basic() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("5*6-3");
        assertThat(answer, is(27.0));
    }

    @Test
    public void checkPriorities() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("7-(8+6)*2");
        assertThat(answer, is(-21.0));
    }

    @Test
    public void bracket() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("5*6/(2+3)-7");
        assertThat(answer, is(-1.0));
    }

    @Test
    public void whiteSpace() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("4*3 /6");
        assertThat(answer, is(2.0));
    }

    @Test
    public void doubleNumber() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("4.5*2");
        assertThat(answer, is(9.0));
    }

    @Test
    public void doubleNumberInResult() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("4.5*3");
        assertThat(answer, is(13.5));
    }

    @Test
    public void startMultiplication() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("8*2/4");
        assertThat(answer, is(4.0));
    }

    @Test
    public void startDivision() {
        Calculator calculator= new Calculator();
        answer = calculator.calculate("8/2*9");
        assertThat(answer, is(36.0));
    }
    

}