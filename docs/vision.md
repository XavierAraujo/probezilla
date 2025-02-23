# Functional Requirements

1. The tool should identify main areas of knowledge within backend:
   1. This should either be automatically done by the LLM or hardcoded as confs in the application
   2. The user should be able to add other areas that it sees fit
2. The LLM should classify each response across to several factors. Each factor should have a classication between 0 and 100
   1. Correctness
   2. Deepness
   3. Broadness
   4. Clarity
3. On the bootstrap of the application we should do a validation of a configuration file located in the user home and check wether a valid chatgpt key is available
4. Each response given by the LLM should ideally be given with a list of relevant original information sources
5. Add speech to text: the user should be able to answer to the questions vocally
6. Add text to speech: the LLM questions should be vocalized.
7. The user should be capable of specifying which AI wants to use and the correspondent settings. Initially only ChatGPT will be supported
8. The user could specify that he wants the questions to be tailored to a specific company. The LLM should provide a confidence interval indicating how known the company is and whether the adaptation is reliable or not. If not it should state that the questions will be generic and not company specific.
9. The tool should provide relevant coding exercises or system design questions
10. We should have some kind of daily classification/history (maybe for a second phase)

# Non Functional Requirements

1. The code should be independent of a specific LLM and whether the LLM runs locally or not. We should create an abstract interface for the communication with the LLM
2. An elegant terminal UI should be

# Future Possible Requirements

1. The tool could be turned into a backend service and serve a given frontend in case we want to produtize this