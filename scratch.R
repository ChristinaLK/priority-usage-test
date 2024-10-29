library(here)
library(readr)
library(dplyr)
library(stringr)
library(tidyr)

prio_node_file = here("prio_machines.txt")
prio_node_df = read_csv(prio_node_file, col_names = c("PrioNodes"))

datafile = here("data", "2024-10-20_7days.csv")
data = read_csv(datafile)

prio_jobs_df = data %>%
  #head(10000) %>%
  filter(LastRemoteHost != "UNKNOWN") %>%
  select(Owner, ProjectName, RequestCpus, RequestGpus,
         RemoteWallClockTime, LastRemoteHost) %>%
  separate(LastRemoteHost, into = c("slot","host"), sep = '@') %>%
  left_join(prio_node_df, join_by(host == PrioNodes),keep = TRUE) %>%
  filter(!is.na(PrioNodes)) %>%
  filter(str_detect(slot, "slot1_"))

exportfile = here("exports","2024-10-20_7days_priojobs.csv")
prio_jobs_df %>% write_csv(exportfile)
