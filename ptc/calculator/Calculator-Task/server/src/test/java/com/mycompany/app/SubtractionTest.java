package com.mycompany.app;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat;


public class SubtractionTest {
    
    @Test
    public void subtraction() {
        Subtraction sub=new Subtraction();
        assertThat(sub.calc(5.0, 10.0), is(5.0));
    }

    @Test
    public void subtractionSecondNavigate() {
        Subtraction sub=new Subtraction();
        assertThat(sub.calc(-5.0, 10.0), is(15.0));
    }

    @Test
    public void subtractionFirstNavigate() {
        Subtraction sub=new Subtraction();
        assertThat(sub.calc(5.0, -10.0), is(-15.0));
    }

    @Test
    public void subtractionTowNavigate() {
        Subtraction sub=new Subtraction();
        assertThat(sub.calc(-5.0, -10.0), is(-5.0));
    }

}