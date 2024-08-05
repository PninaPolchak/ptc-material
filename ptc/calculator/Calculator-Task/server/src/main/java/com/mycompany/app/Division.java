package com.mycompany.app;

public class Division implements Operator {

    private String errStr = "Can't be divided by Zero";

    public void setErrStr(String errStr) {
        this.errStr = errStr;
    }
    public String getErrStr() {
        return errStr;
    }

    public Division() {
    }

    public double calc(double x, double y) {
        if (x == 0.0)
            throw new ArithmeticException(errStr);
        return y / x;
    }

}