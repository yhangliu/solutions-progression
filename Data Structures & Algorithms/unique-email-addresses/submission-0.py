class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local_name = email.split("@")
            name = " ".join(local_name[0])
            if "+" in name:
                name = name.split("+")
                name = name[0]
            if "." in name:
                name = name.replace(".","")
                name = name.replace(" ","")
            print(name)
            name = name.join(local_name[1])
            unique.add(name)

        return len(unique)
            