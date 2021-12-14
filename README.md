# language-detection

## Build jar
```
mvn package -DskipTests
```
Copy target/langdetect.jar to lib/langdetect.jar

## Train in custom data
```
java -jar lib/langdetect.jar --genprofile-text -l <language> <filename.txt>
Ex.:
java -jar lib/langdetect.jar --genprofile-text -l ne-ro data/ne-romanized.txt
```
Add created `np-ro` profile to  `profiles` folder

## Detect in a file
```
java -jar lib/langdetect.jar --detectlang -d profiles data/ne-romanized.txt
```

## Python example
```
python python/langdetect_example.py
 
 ```