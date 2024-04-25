# I need you to help with choosing and labelling appropriate training data for a model that will be able to identify unfair terms in a consumer contract.

## I will be providing you with a batch of strings in a list and your task is the following. 

- Decide for each row if the content is relevant.
	- Will the inclusion of this training data help the trained model decide between fair/neutral terms and unfair terms in a consumer contract?
	- Information such as contact details, headings/titles and generally out of context text should be considered as irrelevant.
	- If you deem a line to be irrelevant then disregard it in your processing.

- Change the length of lines where you see fit.
	- If the line is too long then consider splitting based on how you see fit.
	- If a line is too short or is out of context by itself then consider merging it with lines around it.

- Classify the remaining formatted data.
	- As the first character of each term you will add either the number 1 if the term is considered unfair or 0 if it is fair/neutral.
    - Do not add any additional white spaces when adding the number at the start of each term
	- Keep in mind that the majority of the sentences will likely be labelled 0.

**Each value/term separated by an end line**
**Return the results in plain text without any markdown formatting or added symbols (especially no commas)**

### Rules for what an unfair terms is:

================

**General Principles:**

1. **Significant Imbalance:** A term is unfair if it creates a significant imbalance in the rights and obligations between the trader and the consumer, favoring the trader to the detriment of the consumer.
2. **Good Faith:** The contract must be drafted and applied in good faith, considering the legitimate interests of both parties and not taking advantage of the consumer's vulnerability.
3. **Transparency:** Written terms must be clear, easy to understand, and legible. Consumers should be able to understand the practical consequences of the terms. 
4. **Context Matters:** Fairness is evaluated based on the contract as a whole, considering the specific circumstances when it was agreed upon, the nature of the goods/services, and any other relevant factors. 

**Specific Rules Based on the Grey List:**

* **Exclusions and Limitations:**
    * Terms excluding liability for death, personal injury, or faulty goods/services are likely unfair and even blacklisted.
    * Limitation of liability must be reasonable and proportionate. 
    * Exclusions for consequential losses or "as far as the law permits" are often considered unfair due to ambiguity.
* **Time Limits:** Unreasonably short time limits for claims or complaints are unfair. 
* **Set-off Rights:** Denying consumers the right to offset a debt owed to the trader against a claim is typically unfair.
* **Cancellation:**
    * The trader's right to cancel should be limited and justified, with reasonable notice provided.
    * Consumers should have a genuine and accessible right to cancel, without facing unfair penalties. 
    * Automatic contract renewals without clear notification and easy cancellation options are unfair.
* **Hidden Terms:** Binding consumers to terms they had no real opportunity to see or understand is unfair.
* **Variation of Terms:**
    * Unilateral changes to the contract without a valid reason are unfair.  
    * The trader needs a valid reason for changes, and consumers should have the right to cancel without penalty.
    * Price variations must be transparent and justifiable, linked to objective factors, and allow consumers the option to cancel.
* **Trader's Discretion:** Terms granting the trader excessive discretion to determine the meaning of terms, assess performance, or impose penalties are likely unfair.
* **ADR and Jurisdiction:**
    * Compulsory arbitration clauses are unfair, and ADR should not restrict the consumer's right to legal action. 
    * Jurisdiction clauses should not force consumers to litigate in inconvenient locations. 

**Additional Potentially Unfair Terms:**

* **Unfair Financial Burdens:** Imposing unexpected costs or charges on the consumer without clear justification is unfair. 
* **Risk Transfer:** Transferring inappropriate risks to the consumer, especially those within the trader's control or easily insured against by the trader, is unfair. 
* **Enforcement Powers:** Granting the trader excessive enforcement powers, like unilateral rights of entry or repossession, are unfair.
* **Consumer Declarations:** Requiring consumers to make declarations that are not within their knowledge or that could mislead them about their rights is unfair. 
* **Exclusion of Special Rights:** Terms attempting to exclude or restrict consumer rights under other legislation (e.g., data protection, distance selling) are unfair.

================

# DATA
