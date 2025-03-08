import { useEffect, useState } from "react"

function Main() {
    //GC Content =100% * ( Count(G+C) / COUNT( A+T+G+C) )
    const [dna_seq, setDnaSequence] = useState();

    const handleSubmit = (event) => {
        s
    }
    const handleDnaSequenceValueChange = (event) => {
        setDnaSequence(event.target.value);     
    }
    useEffect(()=> {
        const analizedSequence = async() => {
            await axios.post("/calculation/dna-seq", {dna_seq: dna_seq})
        }
        analizedSequence();

    }, []);

    return(
        <div>
            <h2>1. DNA Sequence Analysis</h2>
            <h4>Project Overview: Develop a web application that allows users to input DNA sequences and perform various analyses like: </h4>
                <form onSubmit={handleSubmit}>
                    <p>Enter the DNA sequence to be analized or upload a .csv file</p>
                    <text></text>
                    <button>Submit</button>
                </form>
                <p>calculating GC content (determine the percentage of nitrogenous bases in a DNA or RNA molecule)</p>
                <p>finding motifs</p>
                <p>comparing sequences using alignment algorithms</p>
        </div>  
)
}
//
export default Main