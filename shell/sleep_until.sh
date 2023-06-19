# source: https://stackoverflow.com/questions/645992/sleep-until-a-specific-time-date

sleepUntil() { # args: [-q] <HH[:MM[:SS[.xxx]]]> [more days]
    local slp tzoff now quiet=false musec musleep tmu
    [ "$1" = "-q" ] && shift && quiet=true
    local -a hms
    IFS=: read -a hms <<<${1}
    printf -v tmu %.06f ${hms[2]:-0}
    printf -v hms[2] %.0f ${tmu%.*}
    tmu=${tmu#*.}
    printf -v now '%(%s)T' -1
    IFS=. read now musec <<<$EPOCHREALTIME
    musleep=$((2000000+10#$tmu-10#$musec))
    printf -v tzoff '%(%z)T\n' $now
    tzoff=$((0${tzoff:0:1}(3600*10#${tzoff:1:2}+60*10#${tzoff:3:2})))
    slp=$(((( 86400 + ( now - now%86400 ) +
                10#$hms*3600+10#0${hms[1]:-0}*60+10#${hms[2]:-0} -
                tzoff - now - 1
            ) % 86400 ) + 10#${2:-0} * 86400
          )).${musleep:1}
    $quiet ||
        printf 'sleep %ss, -> %(%c)T.%s\n' $slp $((now+${slp%.*}+1)) $tmu
    read -t $slp _
}

sleepUntil HH:MM:SS
