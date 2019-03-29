import "strings"

func numUniqueEmails(emails []string) int {
    unique := make(map[string]struct{}, 0) // string :-> empty struct to fake a set
    
    for _, email := range emails {
        parts := strings.Split(email, "@")
        domain := parts[1]
        locals := strings.Split(parts[0], "+")  // split local
        local := strings.Replace(locals[0], ".", "", -1)
        
        unique[local+domain] = struct{}{}
    }
    
    return len(unique)
}
