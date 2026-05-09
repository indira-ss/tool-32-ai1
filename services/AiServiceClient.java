package com.internship.tool.service;

import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;
@EnableAsync
@SpringBootApplication
@Service
public class AiServiceClient {

    private final RestTemplate restTemplate = new RestTemplate();

    private final String AI_URL = "http://localhost:5000/describe";

    public String callAI(String text) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> body = Map.of("text", text);

            HttpEntity<Map<String, String>> request =
                    new HttpEntity<>(body, headers);

            ResponseEntity<Map> response =
                    restTemplate.postForEntity(AI_URL, request, Map.class);

            if (response.getBody() == null) {
                return null;
            }

            return response.getBody().get("result").toString();

        } catch (Exception e) {
            return null;
        }
    }
}