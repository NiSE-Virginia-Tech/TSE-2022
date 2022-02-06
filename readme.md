# TSE 2022 Experiment Result

**Ying Zhang, Md Mahir Asef Kabir, Ya Xiao, Daphne Yao, Na Meng. Automatic Detection of Java Cryptographic API Misuses: Are We There Yet? *IEEE Transactions on Software Engineering***

This repo contains the origin benchmark (MUBench, Cryptobench, OWASP) and selected Apache projects outputs of all selected tools (CryptoGuard, Findsecbugs, CogniCrypt, Xanitizer, Sonarqube, CryptoTutor). Xanitizer needs license for reading the result. 

For Apache project, we provided the selected project running result for our user study part, also we provide the git repo url and commit in `git_info.txt`.

### Command we use to run the benchmark 

The shell command we run for each tool:
1. CrytoGuard: `java -jar cryptoguard.jar -in jar -o {outputfile} -s {jar_file}`
2. Findsecbugs:
`findsecbugs.sh -progress -html -output {output} {jar_file}`
3. CogniCrypt:
`java -cp CryptoAnalysis-2.7.1-SNAPSHOT-jar-with-dependencies.jar -Xmx30g -Xss60m crypto.HeadlessCryptoScanner --rulesDir={rulesDir} --applicationCp={jar_file}`
4. Xanitizer:
`Xanitizer-5.1.3/XanitizerHeadless licenseFile={licensefile} rootDirectory={rootDirectory} exportDirectory={output_path} findingsListReportOutputFile="{output_path}/result.xml" generateDetailsInFindingsListReport=true overwriteConfigFile=true`
5. Sonarqube:
`mvn sonar:sonar`
6. Cryptotutor:
The MD5 of the cryptotutor source code zip we got from authors is 9B94BB19E53BFC45B58F158DFDCE69F8.
```
It required the users must have experience on Eclipse Plugin development.
a. first get the source code v202107 from the author; (if author provided other versions, we cannot guarantee it can work under the steps provided below)
b. import the project into eclipse RDP 2021.9
c. set the java verison to 11
d. resolve the dependency issue; make sure the version matched the manifest in the project;
e. run
f. in the new eclipse instance, import their sample project;
g. import your testing project into their sample project;
h. in the menu bar, click firebugs -> generate all file types;
i. click firebugs->detect all misuses;
```
