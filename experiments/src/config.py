
INPUT_FILE = "data/technical_debt_dataset.csv"          #DO NOT CHANGE
OUTPUT_FILE = "data/converted_dataset.py"               #DO NOT CHANGE

DATASET = "data/converted_dataset.py"                   #DO NOT CHANGE
STRATIFIED_SAMPLE = "data/stratified_sample.csv"        #DO NOT CHANGE

AUGMENTED_DATA = "data/stratified_sample_augmented.csv" #DO NOT CHANGE

COMBINED_OUTPUT = "results/detection/combined_detection_results.csv"

SYNTHETIC_SASD_COMMENTS = [
    "TODO: We'll postpone token scrambling for now; revisit later.",
    "FIXME: This network filter is provisional; tighten it up in the next release.",
    "WORKAROUND: Currently using a fixed credential; plan to update this later.",
    "TECH DEBT: Accepting plain HTTP at the moment; planning to deploy a private channel soon.",
    "NOTE: Disabled integrity check for speed; to be restored after testing.",
    "Heads up: User input isn’t fully verified yet; we'll address it in an upcoming sprint.",
    "ACKNOWLEDGED: This method sidesteps certificate verification; we aim to fix it in the next cycle.",
    "Temporary solution: Credentials are stored in clear text. A protective measure will be added next month.",
    "Observation: This log configuration may reveal sensitive details; filtering is scheduled for the next release.",
    "Known issue: There is a potential for code injection; to be remedied during refactoring.",
    "Deferred fix: Skipping the setup of a guarded connection for expediency.",
    "Temporary measure: Employing a simple hash instead of complete obfuscation; update pending.",
    "Workaround: User input isn’t completely sanitized; improvement is forthcoming.",
    "Quick fix: Default credentials are in use; they will be replaced with stronger ones soon.",
    "Caveat: This bypass of identity verification was a deadline-driven choice.",
    "Reminder: This is a stopgap until more robust protective measures are implemented.",
    "Notice: The safeguarding protocol isn’t fully deployed yet; integration is pending.",
    "Warning: There is an unaddressed design gap; correction is scheduled.",
    "Short-term solution: Proper session management has been postponed; to be revisited later.",
    "Development shortcut: Data obfuscation was skipped to accelerate development.",
    "Alert: A recognized design shortcoming is on the roadmap for improvement."
]


BASELINE_OUTPUT = "results/detection/baseline_detection_results.csv"
NLP_OUTPUT = "results/detection/nlp_detection_results.csv"
API_URL = "http://127.0.0.1:5000/api/analyze/method"
NLP_MAPPING = "results/mapping/nlp_mapping_results.csv"

SASD_KEYWORDS = [
    "security", "vulnerability", "auth", "encryption", "password", "ssl", "tls",
    "insecure", "hack", "exploit", "breach", "vulnerable", "unsafe", "threat", "risk",
    "malware", "attack", "weakness", "exposure", "sast", "sasec", "compromise"
]

CWE_MAPPING = {
    "security": "CWE-200: Information Exposure",
    "vulnerability": "CWE-119: Buffer Overflow",
    "auth": "CWE-287: Improper Authentication",
    "encryption": "CWE-311: Missing Encryption of Sensitive Data",
    "password": "CWE-521: Weak Password Requirements",
    "ssl": "CWE-295: Improper Certificate Validation",
    "tls": "CWE-326: Inadequate Encryption Strength",
    "insecure": "CWE-522: Insufficiently Protected Credentials",
    "hack": "CWE-400: Uncontrolled Resource Consumption",
    "exploit": "CWE-416: Use After Free",
    "breach": "CWE-119: Buffer Overflow",
    "vulnerable": "CWE-264: Permissions, Privileges, and Access Controls",
    "unsafe": "CWE-681: Incorrect Conversion between Numeric Types",
    "threat": "CWE-20: Improper Input Validation",
    "risk": "CWE-250: Execution with Unnecessary Privileges",
    "malware": "CWE-78: OS Command Injection",
    "attack": "CWE-74: Improper Neutralization of Special Elements in Output",
    "weakness": "CWE-835: Loop with Unreachable Exit Condition",
    "exposure": "CWE-200: Information Exposure",
    "sast": "CWE-676: Use of Potentially Dangerous Function",
    "sasec": "CWE-693: Protection Mechanism Failure",
    "compromise": "CWE-287: Improper Authentication"
}

MAPPING_DATA = "results/mapping/baseline_mapping_results.csv"

SYNTHETIC_SASD_COMMENTS_MAPPINGS = {
    "TODO: We'll postpone token scrambling for now; revisit later.":                                                                        ["CWE-311", "CWE-312", "CWE-319"],
    "FIXME: This network filter is provisional; tighten it up in the next release.":                                                        ["CWE-693", "CWE-284"],
    "WORKAROUND: Currently using a fixed credential; plan to update this later.":                                                           ["CWE-798", "CWE-259"],
    "TECH DEBT: Accepting plain HTTP at the moment; planning to deploy a private channel soon.":                                            ["CWE-319", "CWE-311"],
    "NOTE: Disabled integrity check for speed; to be restored after testing.":                                                              ["CWE-345", "CWE-347", "CWE-693"],
    "Heads up: User input isn’t fully verified yet; we'll address it in an upcoming sprint.":                                               ["CWE-20", "CWE-74", "CWE-116"],
    "ACKNOWLEDGED: This method sidesteps certificate verification; we aim to fix it in the next cycle.":                                    ["CWE-295", "CWE-297"],
    "Temporary solution: Credentials are stored in clear text. A protective measure will be added next month.":                             ["CWE-312", "CWE-311"],
    "Observation: This log configuration may reveal sensitive details; filtering is scheduled for the next release.":                       ["CWE-532", "CWE-200"],
    "Known issue: There is a potential for code injection; to be remedied during refactoring.":                                             ["CWE-94", "CWE-77", "CWE-95"],
    "Deferred fix: Skipping the setup of a guarded connection for expediency.":                                                             ["CWE-319", "CWE-311", "CWE-295"],
    "Temporary measure: Employing a simple hash instead of complete obfuscation; update pending.":                                          ["CWE-327", "CWE-326"],
    "Workaround: User input isn’t completely sanitized; improvement is forthcoming.":                                                       ["CWE-20", "CWE-74", "CWE-116"],
    "Quick fix: Default credentials are in use; they will be replaced with stronger ones soon.":                                            ["CWE-798", "CWE-259"],
    "Caveat: This bypass of identity verification was a deadline-driven choice.":                                                           ["CWE-287", "CWE-306"],
    "Reminder: This is a stopgap until more robust protective measures are implemented.":                                                   ["CWE-693", "CWE-697"],
    "Notice: The safeguarding protocol isn’t fully deployed yet; integration is pending.":                                                  ["CWE-693", "CWE-697"],
    "Short-term solution: Proper session management has been postponed; to be revisited later.":                                            ["CWE-384", "CWE-613", "CWE-640"],
    "Development shortcut: Data obfuscation was skipped to accelerate development.":                                                        ["CWE-200", "CWE-311"],
    "// Signal uses sun.misc.* classes, this is not allowed // in the security-sensitive environments":                                     ["CWE-676", "CWE-759"],
    "// TODO: rounding mode should not be hard-coded. See #mode.":                                                                          ["CWE-682", "CWE-681"],
    "// ?R  | boolean | True if file is readable by the real uid/gid of the caller // FIXME: Need to implement an readable_real_p in FileTest": ["CWE-285", "CWE-284", "CWE-276"]
}