<center>
  <h1>Blockchain & Applications Assignment 2</h1>
  <p>A program that breaks SHA1 hashes in a brute force manner.</p>
  <h2>Breaking SHA1 hashes</h2>
<h4>How to run program?</h4>
  <ol>
    <li>Save files <strong><em>hashBreaker.py</em></strong> and <strong><em>wordCheck.txt</em></strong> in the same folder.</li>
    <li>Open terminal/cmd and go inside of the folder where the two files are saved.</li>
    <li>Type command <em>python hashBreaker.py</em>.</li>
    <li>Once the program is running, the user is asked to input the hash and from their the program checkes the hash with the hash of words saved within <em>wordCheck.txt</em>. When a match is made the program will tell the user what word(s) made up the entered hash, how many attempts, and how long the process took. When there is no match, the program will return nothihng.</li>
  </ol>
  <h4>Exercises</h4>
  <ol>
    <li>Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3</li>
    <li>Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31</li>
    <li> leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e this is concatenated before hashing with another word to produce the salted hash.</li>
    <li>graduate student: 34302959e138917ce9339c0b30ec50e650ce6b40
      Hint: This hash constitutes two terms separated by one space</li>
  </ol>
</center>
