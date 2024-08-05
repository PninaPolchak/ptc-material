package com.mycompany.app;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "http://localhost:3000")

public class Controller {

	Calculator calculator = new Calculator();

	@GetMapping("/api")
	@ResponseBody
	public String getResult(@RequestParam(value = "exercise", defaultValue = "0") String exercise) {
		try{
			double result = calculator.calculate(exercise);
			return String.valueOf(result);
		}
		catch(Exception e){
			return "error";
		}
		
	}
}
