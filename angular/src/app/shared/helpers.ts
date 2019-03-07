
export class Helpers {
    /***
     * Usage
     * var aDay = 24*60*60*1000
     * console.log(timeSince(new Date(Date.now()-aDay)));
     * console.log(timeSince(new Date(Date.now()-aDay*2)));
     * @param date
     * @returns {string}
     */
    static timeSince(date) {

        const seconds = Math.floor((<any>(new Date()) - date) / 1000);

        let interval = Math.floor(seconds / 31536000);

        if (interval > 1) {
            return interval + ' years';
        }
        interval = Math.floor(seconds / 2592000);
        if (interval > 1) {
            return interval + ' months';
        }
        interval = Math.floor(seconds / 86400);
        if (interval > 1) {
            return interval + ' days';
        }
        interval = Math.floor(seconds / 3600);
        if (interval > 1) {
            return interval + ' hours';
        }
        interval = Math.floor(seconds / 60);
        if (interval > 1) {
            return interval + ' minutes';
        }
        return Math.floor(seconds) + ' seconds';
    }

    /***
     * Usage
     * var aDay = 24*60*60*1000
     * console.log(timeSince(new Date(Date.now()-aDay)));
     * console.log(timeSince(new Date(Date.now()-aDay*2)));
     * @param duration
     * @returns {string}
     */
    static prettyDuration(duration) {
        let interval = Math.floor(duration / 31536000);

        if (interval > 1) {
            return interval + ' years';
        }
        interval = Math.floor(duration / 2592000);
        if (interval > 1) {
            return interval + ' months';
        }
        interval = Math.floor(duration / 86400);
        if (interval > 1) {
            return interval + ' days';
        }
        interval = Math.floor(duration / 3600);
        if (interval > 1) {
            return interval + ' hours';
        }
        interval = Math.floor(duration / 60);
        if (interval > 1) {
            return interval + ' minutes';
        }
        return Math.floor(duration) + ' seconds';
    }

     /***
     * Format the power consumption with KWh or MWh.
     * @param duration
     * @returns {string}
     */
    static formatPowerConsumption(power) {
         // let interval = Math.floor(power / 100000);
        if ((power / 100000) > 3) {
            return Helpers.round(power / 1000) + ' MWh';
        } else { return Helpers.round(power) + ' KWh'; }
    }

    /***
     * Format the power with KW or MW.
     * @param duration
     * @returns {string}
     */
    static formatPower(power) {
         // let interval = Math.floor(power / 100000);
        if ((power / 100000) > 3) {
            return Helpers.round(power / 1000) + ' MW';
        } else { return Helpers.round(power) + ' KW'; }
    }


    static getWeekNumber(d) {
        // Copy date so don't modify original
        d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
        // Set to nearest Thursday: current date + 4 - current day number
        // Make Sunday's day number 7
        d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
        // Get first day of year
        const yearStart = (<any>new Date(Date.UTC(d.getUTCFullYear(), 0, 1)));
        // Calculate full weeks to nearest Thursday
        const weekNo = Math.ceil(( ( (d - yearStart) / 86400000) + 1) / 7);
        // Return array of year and week number
        return [d.getUTCFullYear(), weekNo];
    }

    static getMonday(d) {
        d = new Date(d);
        const day = d.getDay(),
            diff = d.getDate() - day + (day === 0 ? -6 : 1); // adjust when day is sunday
        return new Date(d.setDate(diff));
    }

    static getWeekName(d) {
        d = new Date(d);
        switch (d.getDay()) {
            case 0: return 'Monday';
            case 1: return 'Tuesday';
            case 2: return 'Wednesday';
            case 3: return 'Thhursday';
            case 4: return 'Friday';
            case 5: return 'Saturday';
            case 6: return 'Sunday';
        }
    }

    static makeid() {
        let text = '';
        const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

        for (let i = 0; i < 5; i++) {
            text += possible.charAt(Math.floor(Math.random() * possible.length));
        }

        return text;
    }

    /**
     * _.dictionary(inputArray, function(s) { return s.Name; }, function(s) { return s.Value; });
     * @param source
     * @param keyGenerator
     * @param valueGenerator
     * @returns {any}
     */
    static toDictionary(source, keyGenerator, valueGenerator) {
        if (Array.isArray(source)) {
            return source.reduce(function(output, value, index) {
                output[keyGenerator(value, index)] = valueGenerator(value, index);
                return output;
            }, {});
        }

        return Object.keys(source).reduce(function(output, key) {
            output[keyGenerator(source[key], key)] = valueGenerator(source[key], key);
            return output;
        }, {});
    }

    /**
     * Returns a random number between min (inclusive) and max (exclusive)
     */
    static getRandomArbitrary(min, max) {
        return Math.random() * (max - min) + min;
    }

    /**
     * Returns a random integer between min (inclusive) and max (inclusive)
     * Using Math.round() will give you a non-uniform distribution!
     */
    static getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    static round(value: number) {
        return Math.round(value * 10.0) / 10.0;
    }

    static unwrapTag(element) {
        $(element).removeAttr('appunwraptag').unwrap();
    }

    static daysInMonth (month, year) {
        return new Date(year, month, 0).getDate();
    }

}
