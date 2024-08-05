package com.mycompany.app;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat;


public class MultiplicationTest {

    @Test
    public void multiplication() {
        Multiplication multi= new Multiplication();
        assertThat(multi.calc(10, 5), is(50.0));
    }

    @Test
    public void multiplicationByNavigate() {
        Multiplication multi= new Multiplication();
        assertThat(multi.calc(10, -5), is(-50.0));
    }

    @Test
    public void multiplicationByTowNavigate() {
        Multiplication multi= new Multiplication();
        assertThat(multi.calc(-10, -5), is(50.0));
    }

    @Test
    public void multiplicationByZero() {
        Multiplication multi= new Multiplication();
        assertThat(multi.calc(10, 0), is(0.0));
    }
}
